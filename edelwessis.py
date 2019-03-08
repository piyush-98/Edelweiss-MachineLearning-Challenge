import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
data=pd.read_excel(r"C:\Users\PIYUSH\Desktop\data\maindata.xlsx",sheet_name=None)
data2=pd.read_excel(r"C:\Users\PIYUSH\Desktop\data\Customers_31JAN2019.xlsx",sheet_name=None)
data3=pd.read_csv(r"C:\Users\PIYUSH\Desktop\data\train_foreclosure.csv")
data4=pd.read_csv(r"C:\Users\PIYUSH\Desktop\data\test_foreclosure.csv")
data_cust=data2['Sheet1']
data_main=data['LMS_HLLAP']
c=0
ls=[]
col=['AGREEMENTID','CUSTOMERID','LOAN_AMT','NET_DISBURSED_AMT','INTEREST_START_DATE','CURRENT_ROI','ORIGNAL_ROI','CURRENT_TENOR','ORIGNAL_TENOR','DUEDAY','AUTHORIZATIONDATE','CITY','PRE_EMI_DUEAMT',	'PRE_EMI_RECEIVED_AMT','PRE_EMI_OS_AMOUNT','EMI_DUEAMT','EMI_RECEIVED_AMT','EMI_OS_AMOUNT','EXCESS_AVAILABLE','EXCESS_ADJUSTED_AMT','BALANCE_EXCESS','NET_RECEIVABLE','OUTSTANDING_PRINCIPAL','PAID_PRINCIPAL','PAID_INTEREST','MONTHOPENING','LAST_RECEIPT_DATE','LAST_RECEIPT_AMOUNT','NET_LTV','COMPLETED_TENURE','BALANCE_TENURE','DPD','FOIR','PRODUCT	SCHEMEID','NPA_IN_LAST_MONTH','NPA_IN_CURRENT_MONTH','MOB']
test_data=pd.DataFrame(columns=col)
for i in (data_main["AGREEMENTID"]):
    if i in list(data4["AGREEMENTID"]):
        c=list(data_main["AGREEMENTID"]).index(i)
        ls.append(c)
        test_data=test_data.append(data_main.loc[c],ignore_index=True)
        print(test_data.shape)
filename=r"C:\Users\PIYUSH\Desktop\edel.pkl"
filename2=r"C:\Users\PIYUSH\Desktop\edel2.pkl"
test_data.to_pickle(file_name)
data_main.drop(data_main.index[ls], inplace=True)

data_main.to_pickle(file_name2)
print(len(ls))
