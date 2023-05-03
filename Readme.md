Welcome to AmazeKart Analytics. 

Run followung commands to make apis online:

1. pip install -r requirements.txt
2. uvicorn main:app --reload

API's available:
1. SalesAnalysis:
- Analysis of the total sales based on the label provided.
- Sample input: {"12 March":10, "15 March": 56, "30 March": 50}

2. ProductAnalysis:
- Analysis the total product that got sold in the data provided.
- Sample input: {"Product": ["Milk", "Bread", "Eggs", "Milk", "Biscuits"], "Sale": [5, 2, 10, 10, 50]}
