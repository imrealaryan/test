import pandas as pd
import numpy as ny
bureau_data = pd.read_excel("C:/Users/Aditi Jain/OneDrive/Desktop/aryan jain/Ratul Paul Sir/home-credit-default-risk/Made by me/recoded_bureau_balance5k.xlsx")
#On using BaseCode in Bureau_Balance_L3MdivL12M_5715448_Momentum#BaseCodeOnly.txt
#Momentum 1 Function Name Ln1M_Ln2M_DPDSp_ratio
def Ln1M_Ln2M_DPDSp_ratio(i,n1,n2,s):
    Customer_SKID = bureau_data[bureau_data["SK_ID_BUREAU"]==i]
    #n1 is month value for numerator month
    Ln1M = Customer_SKID[Customer_SKID["MONTHS_BALANCE"] > -n1] 
    Ln1M_DPD0p_count = Ln1M[Ln1M["STATUS"] > s]
    Ln1M_DPD0p_count_length = len(Ln1M_DPD0p_count)
    #n2 is month value for denominator month
    Ln2M = Customer_SKID[Customer_SKID["MONTHS_BALANCE"] > -n2] 
    Ln2M_DPD0p_count = Ln2M[Ln2M["STATUS"] > s]
    Ln2M_DPD0p_count_length = len(Ln2M_DPD0p_count)
    if Ln2M_DPD0p_count_length==0:
      output = -999
    else:
      output = (Ln1M_DPD0p_count_length/Ln2M_DPD0p_count_length)
    return output
#Momentum 2
def Ln1M_Ln2M_DPDS_ratio(i,n1,n2,s):
    Customer_SKID = bureau_data[bureau_data["SK_ID_BUREAU"]==i]
    #n1 is month value for numerator month
    Ln1M = Customer_SKID[Customer_SKID["MONTHS_BALANCE"] > -n1] 
    Ln1M_DPDS_count = Ln1M[Ln1M["STATUS"] == s]
    Ln1M_DPDS_count_length = len(Ln1M_DPDS_count)
    #n2 is month value for denominator month
    Ln2M = Customer_SKID[Customer_SKID["MONTHS_BALANCE"] > -n2] 
    Ln2M_DPDS_count = Ln2M[Ln2M["STATUS"] == s]
    Ln2M_DPDS_count_length = len(Ln2M_DPDS_count)
    if Ln2M_DPDS_count_length==0:
      output = -999
    else:
      output = (Ln1M_DPDS_count_length/Ln2M_DPDS_count_length)
    return output
#Flag function 1
def LnM_DPDSp_flag(i,month,s):
    Customer_SKID = bureau_data[bureau_data["SK_ID_BUREAU"]==i]
    LnM = Customer_SKID[Customer_SKID["MONTHS_BALANCE"] > -month] 
    LnM_DPD0p_flag = LnM[LnM["STATUS"] > s]
    if len(LnM_DPD0p_flag) > 0 :
        output = 1
    else:
        output = 0
    return output
#List of SK_ID_BUREAU
Unique_SKID = bureau_data["SK_ID_BUREAU"].unique().tolist()
#Momentum Blank lists
L3M_L12M_DPD0p_ratio_list = []
L3M_L12M_DPD1_ratio_list = []
#Flag Quarterly lists
L3M_list = []
L6M_list = []
L9M_list = []
L12M_list = []
L15M_list = []
L18M_list = []
L21M_list = []
L24M_list = []
L27M_list = []
L30M_list = []
L33M_list = []
L36M_list = []
#Loop
for i in Unique_SKID:
    #Momentum Features
    y1 = Ln1M_Ln2M_DPDSp_ratio(i,4,13,0)
    L3M_L12M_DPD0p_ratio_list.append(y1)
    y2 = Ln1M_Ln2M_DPDS_ratio(i,4,13,1)
    L3M_L12M_DPD1_ratio_list.append(y2)
    #Flag Features
    x1=LnM_DPDSp_flag(i,4,0)
    L3M_list.append(x1)
    x2=LnM_DPDSp_flag(i,7,0)
    L6M_list.append(x2)
    x3=LnM_DPDSp_flag(i,10,0)
    L9M_list.append(x3)
    x4=LnM_DPDSp_flag(i,13,0)
    L12M_list.append(x4)
    x5=LnM_DPDSp_flag(i,16,0)
    L15M_list.append(x5)
    x6=LnM_DPDSp_flag(i,19,0)
    L18M_list.append(x6)
    x7=LnM_DPDSp_flag(i,22,0)
    L21M_list.append(x7)
    x8=LnM_DPDSp_flag(i,25,0)
    L24M_list.append(x8)
    x9=LnM_DPDSp_flag(i,28,0)
    L27M_list.append(x9)
    x10=LnM_DPDSp_flag(i,31,0)
    L30M_list.append(x10)
    x11=LnM_DPDSp_flag(i,34,0)
    L33M_list.append(x11)
    x12=LnM_DPDSp_flag(i,37,0)
    L36M_list.append(x12)
