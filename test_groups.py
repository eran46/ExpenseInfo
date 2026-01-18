#!/usr/bin/env python3
"""
Test script for groups infrastructure
Run this to verify the groups feature is working correctly
"""

from groups_manager import GroupsManager
from data_manager import DataManager
from user_expense_calculator import UserExpenseCalculator


def test_groups_infrastructure():
    """Test basic groups functionality"""
    print("=" * 60)
    print("Testing Groups Infrastructure")
    print("=" * 60)
    
    # Initialize groups manager
    print("\n1. Initializing GroupsManager...")
    gm = GroupsManager()
    print("   ✓ GroupsManager initialized")
    
    # Check for existing groups
    print("\n2. Checking for existing groups...")
    groups = gm.get_all_groups()
    print(f"   Found {len(groups)} existing group(s)")
    
    if not groups:
        print("\n3. No groups found. Testing migration...")
        # Check if old data exists
        import os
        if os.path.exists("user_data/transactions.json"):
            print("   Old transactions.json found, migrating...")
            migrated = gm.migrate_existing_data()
            if migrated:
                print("   ✓ Migration successful!")
                groups = gm.get_all_groups()
            else:
                print("   Already migrated or no data to migrate")
        else:
            print("   No old data to migrate")
            print("\n4. Creating test group...")
            group = gm.create_group(
                name="Test Group",
                description="Test group for verification",
                emoji="🧪",
                members=["Person 1", "Person 2"]
            )
            print(f"   ✓ Created group: {group['emoji']} {group['name']}")
            groups = gm.get_all_groups()
    
    # Display groups
    print(f"\n5. Current groups ({len(groups)}):")
    for g in groups:
        print(f"   - {g['emoji']} {g['name']}: {g['description']}")
        print(f"     ID: {g['id']}")
        print(f"     Members: {', '.join(g['members']) if g['members'] else 'None'}")
        print(f"     Path: {gm.get_group_data_path(g['id'])}")
    
    # Test active group
    print("\n6. Testing active group...")
    active = gm.get_active_group()
    if active:
        print(f"   Active group: {active['emoji']} {active['name']}")
    else:
        print("   No active group set")
    
    # Test DataManager with group path
    if groups:
        print("\n7. Testing DataManager with group path...")
        group_path = gm.get_group_data_path(groups[0]['id'])
        dm = DataManager(group_path)
        print(f"   ✓ DataManager initialized for: {groups[0]['name']}")
        
        if dm.data_exists():
            df = dm.get_dataframe()
            print(f"   Data file exists: {len(df)} transactions")
            
            # Check for member columns
            member_cols = dm.get_member_columns(df)
            if member_cols:
                print(f"   Member columns found: {', '.join(member_cols)}")
                
                # Test UserExpenseCalculator
                print("\n8. Testing UserExpenseCalculator...")
                calc = UserExpenseCalculator(gm)
                
                member = member_cols[0]
                expenses = calc.calculate_user_total_expense([groups[0]['id']], member)
                print(f"   Member: {member}")
                print(f"   Total Expense: ₪{expenses['total_expense']:,.2f}")
                print(f"   Transactions: {expenses['transaction_count']}")
                
                # Category breakdown
                categories = calc.get_member_expense_by_category([groups[0]['id']], member)
                if categories:
                    print(f"   Top 3 categories:")
                    sorted_cats = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:3]
                    for cat, amt in sorted_cats:
                        print(f"     - {cat}: ₪{amt:,.2f}")
            else:
                print("   No member columns found in data")
        else:
            print("   No transaction data in group yet")
    
    print("\n" + "=" * 60)
    print("✓ Groups infrastructure test complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Update app.py to use groups")
    print("2. Add group selector UI")
    print("3. Update data management page")
    print("4. Add combined analytics page")


if __name__ == "__main__":
    test_groups_infrastructure()
