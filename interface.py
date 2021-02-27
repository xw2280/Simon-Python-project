# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import base64
import numpy as np
import pickle
import altair as alt
from PIL import Image
import matplotlib.pyplot as plt
from annotated_text import annotated_text, annotation

#change the file path on your own laptop




image = Image.open('/Users/rachelwu/Desktop/proto/pic1.png')
st.image(image, use_column_width=True)
st.title('Home Equity Line of Credit Evaluation - The Best Decision Support System')
st.markdown("<h3 style='text-align: center; color: blue;'>Designed by MSMA Team: Xinnan Wu, Meg Liao, Leo Li, Bing Li, Ying Zhu\n</h3>", unsafe_allow_html=True)
# Load sample data
df = pd.read_csv('/Users/rachelwu/Desktop/proto/heloc_dataset_v1.csv')

# Load the model.
filename = '/Users/rachelwu/Desktop/proto/model_meg.sav'
with open(filename, 'rb') as f:
	loaded_model = pickle.load(f)

st.write('**Please slide to input values:**')

# Select the input values of the features.
st.subheader("Please input value: ")

ExternalRiskEstimate = st.number_input('External Risk Estimate:')
MSinceOldestTradeOpen = st.number_input('Months Since Oldest Trade Open:')
MSinceMostRecentTradeOpen = st.number_input('Months Since Most Recent Trade Open:')
AverageMInFile = st.number_input('Average Months in File:')
NumSatisfactoryTrades = st.number_input('Number Satisfactory Trades:')
NumTrades60Ever2DerogPubRec = st.number_input('Number Trades 60+ Ever:')
NumTrades90Ever2DerogPubRec = st.number_input('Number Trades 90+ Ever:')
PercentTradesNeverDelq = st.slider('Percent Trades Never Delinquent:', 0, 100)
MSinceMostRecentDelq = st.number_input('Months Since Most Recent Delinquency:')
MaxDelq2PublicRecLast12M = st.selectbox('Max Delq/Public Records Last 12 Months:',
                                        [0,1,2,3,4,5,6,7,8,9])
MaxDelqEver = st.selectbox('Max Delinquency Ever:',
                          [2,3,4,5,6,7,8,9])
NumTotalTrades = st.number_input('Number of Total Trades (total number of credit accounts):')
NumTradesOpeninLast12M = st.number_input('Number of Trades Open in Last 12 Months:')
PercentInstallTrades = st.slider('Percent Installment Trades:', 0, 100)
MSinceMostRecentInqexcl7days = st.number_input('Months Since Most Recent Inq excl 7days:')
NumInqLast6M = st.number_input('Number of Inq Last 6 Months:')
NumInqLast6Mexcl7days = st.number_input('Number of Inq Last 6 Months excl 7days:')
NetFractionRevolvingBurden = st.number_input('Net Fraction Revolving Burden:')
NetFractionInstallBurden = st.number_input('Net Fraction Installment Burden:')
NumRevolvingTradesWBalance = st.number_input('Number Revolving Trades with Balance:')
NumInstallTradesWBalance = st.number_input('Number Installment Trades with Balance:')
NumBank2NatlTradesWHighUtilization = st.number_input('Number Bank/Natl Trades w high utilization ratio:')
PercentTradesWBalance = st.slider('Percent Trades with Balance:', 0, 100)

x = pd.DataFrame({'External Risk Estimate:':ExternalRiskEstimate,
                    'Months Since Oldest Trade Open:':MSinceOldestTradeOpen,
                    'Months Since Most Recent Trade Open:':MSinceMostRecentTradeOpen,
                  'Average Months in File:':AverageMInFile,
                  'Number Satisfactory Trades:':NumSatisfactoryTrades,
                  'Number Trades 60+ Ever:':NumTrades60Ever2DerogPubRec,
                  'Number Trades 90+ Ever:':NumTrades90Ever2DerogPubRec,
                  'Percent Trades Never Delinquent:':PercentTradesNeverDelq,
                  'Months Since Most Recent Delinquency:':MSinceMostRecentDelq,
                  'Max Delq/Public Records Last 12 Months:':MaxDelq2PublicRecLast12M,
                  'Max Delinquency Ever:':MaxDelqEver,
                  'Number of Total Trades (total number of credit accounts):':NumTotalTrades,
                  'Number of Trades Open in Last 12 Months:':NumTradesOpeninLast12M,
                  'Percent Installment Trades:':PercentInstallTrades,
                  'Months Since Most Recent Inq excl 7days:':MSinceMostRecentInqexcl7days,
                  'Number of Inq Last 6 Months:':NumInqLast6M,
                  'Number of Inq Last 6 Months excl 7days:':NumInqLast6Mexcl7days,
                  'Net Fraction Revolving Burden':NetFractionRevolvingBurden,
                  'Net Fraction Installment Burden:':NetFractionInstallBurden,
                  'Number Revolving Trades with Balance:':NumRevolvingTradesWBalance,
                  'Number Installment Trades with Balance:':NumInstallTradesWBalance,
                  'Number Bank/Natl Trades w high utilization ratio:':NumBank2NatlTradesWHighUtilization,
                  'Percent Trades with Balance:':PercentTradesWBalance},index=[0])

# Output the predit value.
yp = loaded_model.predict(x)
if yp == 1:
    st.error('Risk performance is Bad')
else:
    st.success('Risk performance is Good')
