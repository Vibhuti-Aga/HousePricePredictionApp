import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
with open("C:/Users/Dell/HPP/model.pkl", 'rb') as file:
    model = pickle.load(file)

st.title("🏡 House Price Prediction App")

def main():
    st.markdown("Fill in the details below to predict the selling price of a house.")

    # --- Categorical Inputs ---
    MSZoning = st.selectbox("Zoning Classification", ['RL', 'RM', 'FV', 'RH', 'C (all)'])
    LotShape = st.selectbox("Lot Shape", ['Reg', 'IR1', 'IR2', 'IR3'])
    LandContour = st.selectbox("Land Contour", ['Lvl', 'Bnk', 'HLS', 'Low'])
    LotConfig = st.selectbox("Lot Configuration", ['Inside', 'Corner', 'CulDSac', 'FR2', 'FR3'])
    LandSlope = st.selectbox("Land Slope", ['Gtl', 'Mod', 'Sev'])
    Neighborhood = st.selectbox("Neighborhood", ['CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel', 'Somerst', 'Other'])
    Condition1 = st.selectbox("Condition 1", ['Norm', 'Feedr', 'Artery', 'RRAn', 'PosN', 'Other'])
    BldgType = st.selectbox("Building Type", ['1Fam', '2fmCon', 'Duplex', 'TwnhsE', 'Twnhs'])
    HouseStyle = st.selectbox("House Style", ['1Story', '2Story', '1.5Fin', 'SLvl', 'Other'])
    RoofStyle = st.selectbox("Roof Style", ['Gable', 'Hip', 'Gambrel', 'Mansard', 'Other'])
    Exterior1st = st.selectbox("Exterior Covering 1", ['VinylSd', 'MetalSd', 'Wd Sdng', 'HdBoard', 'BrkFace', 'Other'])
    Exterior2nd = st.selectbox("Exterior Covering 2", ['VinylSd', 'MetalSd', 'Wd Sdng', 'HdBoard', 'Other'])
    MasVnrType = st.selectbox("Masonry Veneer Type", ['None', 'BrkFace', 'Stone', 'BrkCmn'])
    ExterQual = st.selectbox("Exterior Quality", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
    ExterCond = st.selectbox("Exterior Condition", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
    Foundation = st.selectbox("Foundation Type", ['PConc', 'CBlock', 'BrkTil', 'Slab', 'Other'])
    BsmtQual = st.selectbox("Basement Quality", ['Ex', 'Gd', 'TA', 'Fa', 'None'])
    BsmtCond = st.selectbox("Basement Condition", ['Gd', 'TA', 'Fa', 'Po', 'None'])
    BsmtExposure = st.selectbox("Basement Exposure", ['Gd', 'Av', 'Mn', 'No', 'None'])
    BsmtFinType1 = st.selectbox("Basement Finish Type 1", ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', 'None'])
    BsmtFinType2 = st.selectbox("Basement Finish Type 2", ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', 'None'])
    HeatingQC = st.selectbox("Heating Quality & Condition", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
    CentralAir = st.radio("Central Air Conditioning", ['Y', 'N'])
    Electrical = st.selectbox("Electrical System", ['SBrkr', 'FuseA', 'FuseF', 'FuseP', 'Mix'])
    KitchenQual = st.selectbox("Kitchen Quality", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
    Functional = st.selectbox("Home Functional Condition", ['Typ', 'Min1', 'Min2', 'Mod', 'Maj1', 'Maj2', 'Sev', 'Sal'])
    FireplaceQu = st.selectbox("Fireplace Quality", ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'None'])
    GarageType = st.selectbox("Garage Type", ['Attchd', 'Detchd', 'BuiltIn', 'Basment', 'CarPort', 'None'])
    GarageFinish = st.selectbox("Garage Finish", ['Fin', 'RFn', 'Unf', 'None'])
    GarageQual = st.selectbox("Garage Quality", ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'None'])
    GarageCond = st.selectbox("Garage Condition", ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'None'])
    PavedDrive = st.selectbox("Paved Driveway", ['Y', 'P', 'N'])
    SaleType = st.selectbox("Sale Type", ['WD', 'New', 'COD', 'ConLD', 'Other'])
    SaleCondition = st.selectbox("Sale Condition", ['Normal', 'Abnorml', 'Partial', 'Family', 'Alloca', 'AdjLand'])

    # --- Numerical Inputs ---
    LotFrontage = st.number_input("Lot Frontage")
    LotArea = st.number_input("Lot Area (sqft)")
    MasVnrArea = st.number_input("Masonry Veneer Area")
    BsmtFinSF1 = st.number_input("Basement Finished Area 1")
    BsmtUnfSF = st.number_input("Basement Unfinished Area")
    GrLivArea = st.number_input("Above Ground Living Area")
    BedroomAbvGr = st.number_input("Bedrooms Above Ground")
    KitchenAbvGr = st.number_input("Kitchens Above Ground")
    TotRmsAbvGrd = st.number_input("Total Rooms Above Ground")
    Fireplaces = st.number_input("Number of Fireplaces")
    GarageCars = st.number_input("Garage Capacity (Cars)")
    GarageArea = st.number_input("Garage Area (sqft)")
    WoodDeckSF = st.number_input("Wood Deck Area")
    OpenPorchSF = st.number_input("Open Porch Area")
    RemodelAge = st.number_input("Years Since Remodel")
    HouseAge = st.number_input("House Age (Years)")
    TotalBath = st.number_input("Total Bathrooms")
    TotalSF = st.number_input("Total Square Footage")
    GarageAge = st.number_input("Garage Age (Years)")

    # --- Add missing inputs ---
    OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)
    OverallCond = st.slider("Overall Condition (1-10)", 1, 10, 5)

    input_dict = {
        'MSZoning': MSZoning,
        'LotFrontage': LotFrontage,
        'LotArea': LotArea,
        'LotShape': LotShape,
        'LandContour': LandContour,
        'LotConfig': LotConfig,
        'LandSlope': LandSlope,
        'Neighborhood': Neighborhood,
        'Condition1': Condition1,
        'BldgType': BldgType,
        'HouseStyle': HouseStyle,
        'OverallQual': OverallQual,
        'OverallCond': OverallCond,
        'RoofStyle': RoofStyle,
        'Exterior1st': Exterior1st,
        'Exterior2nd': Exterior2nd,
        'MasVnrType': MasVnrType,
        'MasVnrArea': MasVnrArea,
        'ExterQual': ExterQual,
        'ExterCond': ExterCond,
        'Foundation': Foundation,
        'BsmtQual': BsmtQual,
        'BsmtCond': BsmtCond,
        'BsmtExposure': BsmtExposure,
        'BsmtFinType1': BsmtFinType1,
        'BsmtFinSF1': BsmtFinSF1,
        'BsmtFinType2': BsmtFinType2,
        'BsmtUnfSF': BsmtUnfSF,
        'HeatingQC': HeatingQC,
        'CentralAir': CentralAir,
        'Electrical': Electrical,
        'GrLivArea': GrLivArea,
        'BedroomAbvGr': BedroomAbvGr,
        'KitchenAbvGr': KitchenAbvGr,
        'KitchenQual': KitchenQual,
        'TotRmsAbvGrd': TotRmsAbvGrd,
        'Functional': Functional,
        'Fireplaces': Fireplaces,
        'FireplaceQu': FireplaceQu,
        'GarageType': GarageType,
        'GarageFinish': GarageFinish,
        'GarageCars': GarageCars,
        'GarageArea': GarageArea,
        'GarageQual': GarageQual,
        'GarageCond': GarageCond,
        'PavedDrive': PavedDrive,
        'WoodDeckSF': WoodDeckSF,
        'OpenPorchSF': OpenPorchSF,
        'SaleType': SaleType,
        'SaleCondition': SaleCondition,
        'RemodelAge': RemodelAge,
        'HouseAge': HouseAge,
        'TotalBath': TotalBath,
        'TotalSF': TotalSF,
        'GarageAge': GarageAge
    }

    input_df = pd.DataFrame([input_dict])

    if st.button("Predict Sale Price 💰"):
        prediction = model.predict(input_df)
        st.success(f"🏠 Estimated Sale Price: ₹{int(prediction[0]):,}")

if __name__ == '__main__':
    main()
