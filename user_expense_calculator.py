import pandas as pd
from typing import List, Dict, Tuple, Optional
from groups_manager import GroupsManager
from data_manager import DataManager


class UserExpenseCalculator:
    """Calculate per-user expenses across single or multiple groups"""
    
    def __init__(self, groups_manager: GroupsManager):
        self.groups_manager = groups_manager
    
    def calculate_user_total_expense(self, group_ids: List[str], member_name: str, 
                                    date_range: Optional[Tuple] = None) -> Dict:
        """
        Calculate total expense for a specific user across groups.
        
        This calculates the actual expense (share of cost), not just contributions.
        For split transactions, this is their portion of the total cost.
        
        Args:
            group_ids: List of group IDs to analyze
            member_name: Name of the member to calculate expenses for
            date_range: Optional tuple of (start_date, end_date) for filtering
            
        Returns:
            Dictionary with expense breakdown and transaction list
        """
        total_expense = 0
        total_paid = 0
        total_owed_to_them = 0
        transactions = []
        
        for group_id in group_ids:
            group = self.groups_manager.get_group_by_id(group_id)
            if not group:
                continue
                
            group_path = self.groups_manager.get_group_data_path(group_id)
            if not group_path:
                continue
                
            dm = DataManager(group_path)
            
            try:
                df = dm.get_dataframe()
            except Exception:
                continue
            
            if df.empty or member_name not in df.columns:
                continue
            
            # Filter by date range if provided
            if date_range:
                df = df[(df['Date'] >= pd.to_datetime(date_range[0])) & 
                       (df['Date'] <= pd.to_datetime(date_range[1]))]
            
            # Get member's transactions
            member_transactions = dm.get_member_transactions(df, member_name)
            
            for _, txn in member_transactions.iterrows():
                member_amount = txn[member_name]
                
                # Splitwise format:
                # Positive value = Person PAID this amount (their actual expense)
                # Negative value = Person OWES this amount (debt to whoever paid)
                if member_amount > 0:
                    # They paid this amount - it's their expense
                    total_expense += member_amount
                    total_paid += member_amount
                elif member_amount < 0:
                    # They owe this amount - someone else paid
                    # This means they're in debt, not that they're owed money
                    total_owed_to_them += abs(member_amount)
                
                transactions.append({
                    'group_id': group_id,
                    'group_name': group['name'],
                    'date': txn['Date'],
                    'description': txn['Description'],
                    'category': txn['Category'],
                    'total_cost': txn['Cost'],
                    'member_share': member_amount,
                    'is_debt': member_amount < 0
                })
        
        # Calculate net balance correctly:
        # If person paid more than they owe, they are OWED money (negative balance)
        # If person owes more than they paid, they OWE money (positive balance)
        # But in Splitwise: positive paid, negative owed
        # So net = paid - owed. If positive, they're owed. If negative, they owe.
        net_balance = total_paid - total_owed_to_them
        
        return {
            'member_name': member_name,
            'total_expense': total_expense,  # What they actually paid
            'total_owed_by_them': total_owed_to_them,  # What they owe to others
            'net_balance': net_balance,  # Positive = they're owed, Negative = they owe
            'transactions': transactions,
            'transaction_count': len(transactions),
            'groups_analyzed': len(group_ids)
        }
    
    def calculate_all_members_expenses(self, group_ids: List[str], 
                                      date_range: Optional[Tuple] = None) -> Dict[str, Dict]:
        """Calculate expenses for all members across specified groups"""
        all_members = self.groups_manager.get_all_members_across_groups(group_ids)
        
        results = {}
        for member in all_members:
            results[member] = self.calculate_user_total_expense(
                group_ids, member, date_range
            )
        
        return results
    
    def get_member_expense_by_category(self, group_ids: List[str], member_name: str) -> Dict[str, float]:
        """Break down member's expenses by category"""
        category_breakdown = {}
        
        for group_id in group_ids:
            group_path = self.groups_manager.get_group_data_path(group_id)
            if not group_path:
                continue
                
            dm = DataManager(group_path)
            
            try:
                df = dm.get_dataframe()
            except Exception:
                continue
            
            if df.empty or member_name not in df.columns:
                continue
            
            member_txns = dm.get_member_transactions(df, member_name)
            
            for _, txn in member_txns.iterrows():
                category = txn['Category']
                member_amount = txn[member_name]
                
                # Only count positive amounts (what they actually paid)
                if member_amount > 0:
                    if category not in category_breakdown:
                        category_breakdown[category] = 0
                    category_breakdown[category] += member_amount
        
        return category_breakdown
    
    def get_member_expense_by_group(self, group_ids: List[str], member_name: str) -> Dict[str, float]:
        """Break down member's expenses by group"""
        group_breakdown = {}
        
        for group_id in group_ids:
            group = self.groups_manager.get_group_by_id(group_id)
            if not group:
                continue
            
            member_stats = self.calculate_user_total_expense([group_id], member_name)
            group_breakdown[group['name']] = member_stats['total_expense']
        
        return group_breakdown
    
    def get_member_monthly_expenses(self, group_ids: List[str], member_name: str) -> pd.DataFrame:
        """Get member's monthly expense breakdown"""
        all_transactions = []
        
        for group_id in group_ids:
            group_path = self.groups_manager.get_group_data_path(group_id)
            if not group_path:
                continue
                
            dm = DataManager(group_path)
            
            try:
                df = dm.get_dataframe()
            except Exception:
                continue
            
            if df.empty or member_name not in df.columns:
                continue
            
            member_txns = dm.get_member_transactions(df, member_name)
            
            for _, txn in member_txns.iterrows():
                if txn[member_name] > 0:  # Only actual expenses
                    all_transactions.append({
                        'Date': txn['Date'],
                        'Amount': txn[member_name],
                        'Category': txn['Category']
                    })
        
        if not all_transactions:
            return pd.DataFrame()
        
        df = pd.DataFrame(all_transactions)
        df['YearMonth'] = df['Date'].dt.to_period('M')
        monthly = df.groupby('YearMonth')['Amount'].sum().reset_index()
        monthly['YearMonth'] = monthly['YearMonth'].astype(str)
        
        return monthly
