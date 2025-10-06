# Living Expense Category Dropdown - To Be Added

**Field Name**: Living Expense Category
**Selector**: `button.dropdown-toggle:has-text('Living Expense')` (trigger)
**Section**: Financials - Living Expenses
**Option Count**: 21
**Type**: Custom Bootstrap Dropdown

## Complete Options List

```
1.  Transport
2.  Rent
3.  Board
4.  Groceries
5.  Childcare
6.  Child & Spouse Maintenance
7.  Clothing & Personal Care
8.  Public or Government Primary & Secondary Education
9.  Higher Education & Vocational Training (excluding HECS/HELP)
10. Private & Non-Government Education
11. General Insurance (Including Home & Contents on Primary O/Occ Residence)
12. Personal Insurance (Life, Health, Sickness and Personal Accident)
13. Other Insurances
14. Investment Property Costs (including Insurance)
15. Primary Residence Costs (excluding Insurance)
16. Secondary Residence & Holiday Home Costs (including Insurance)
17. O/Occ Strata, Body Corporate, Land Tax
18. Medical & Health (excluding Health Insurance)
19. Other Regular and Recurring Expenses
20. Recreation & Entertainment
21. Telephone, Internet, Pay TV & Media Streaming Subscriptions
```

## Notes

- This is a **dynamic dropdown** - clicking the trigger button adds a new expense row
- Each row requires: Category (dropdown), Frequency (dropdown), Amount (text input)
- The selector pattern is custom and requires click to open, then select from list
- Mappings file (`expense_mappings.json`) contains 147 variations for fuzzy matching

## TODO

- [ ] Add this section to `COMPLETE_CONNECTIVE_CRM_REFERENCE.md`
- [ ] Update element count in executive summary
- [ ] Test MCP server recognizes the new field
