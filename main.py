from typing import Optional
import json
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
import pandas as pd


app = FastAPI()

@app.post("/sales")
async def SalesAnalysis(request: Request):
    # Expects input eg: {"12 March":10, "15 March": 56, "30 March": 50}
    data = await request.json()
    df = pd.DataFrame.from_dict(data, orient='index')
    plot = df.plot(kind='bar')
    fig = plot.get_figure()
    fig.savefig("./analysis/sales.png")
    return True

@app.post("/product")
async def ProductAnalysis(request: Request):
    # Expects input eg: {"Product": ["Milk", "Bread", "Eggs", "Milk", "Biscuits"], "Sale": [5, 2, 10, 10, 50]}
    data = await request.json()
    df = pd.DataFrame.from_dict(data)
    print(df)
    plot = df.groupby(['Product']).sum().plot(kind='pie', y='Sale')
    fig = plot.get_figure()
    fig.savefig("./analysis/product.png")
    return True