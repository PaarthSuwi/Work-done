import pandas as pd
import numpy as np
import yfinance as yf
from ta import add_all_ta_features
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import plotly.graph_objs as go
from datetime import datetime

tickerSymbol = "AMZN"
start_date = '2022-05-09'
end_date = '2023-05-09'

ticker_data = yf.Ticker(tickerSymbol)
df = ticker_data.history(start=start_date, end=end_date)

print(df.columns)
print('-----------------------')
print('Done!')

df = add_all_ta_features(df, "Open", "High", "Low", "Close", "Volume", fillna=True)
df = pd.read_csv('AMZN.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Hour'] = df['Date'].dt.hour
df['Month'] = df['Date'].dt.month
df['Weekday'] = df['Date'].dt.weekday
df['hour_sin'] = np.sin(2 * np.pi * df['Hour'] / 24)
df['hour_cos'] = np.cos(2 * np.pi * df['Hour'] / 24)
df['month_sin'] = np.sin(2 * np.pi * df['Month'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['Month'] / 12)
df['weekday_sin'] = np.sin(2 * np.pi * df['Weekday'] / 7)
df['weekday_cos'] = np.cos(2 * np.pi * df['Weekday'] / 7)
df.drop(['Hour', 'Month', 'Weekday'], axis=1, inplace=True)


shifts = [1, 5, 10]
train_pct = 0.75

window_size = 16

chart_height = 500
chart_width = 800

date_format = '%Y-%m-%d'

def create_ma_feature(df, window_size):
    df['ma'] = df['Close'].rolling(window_size).mean()
    return df

def create_ema_feature(df, window_size):
    df['ema'] = df['Close'].ewm(span=window_size, adjust=False).mean()
    return df

def create_lagged_features(df, shifts):
    for shift in shifts:
        df[f'close_lag_{shift}'] = df['Close'].shift(shift)
    return df.dropna()

df = create_ma_feature(df, window_size)
df = create_ema_feature(df, window_size)

df = create_lagged_features(df, shifts)
train_size = int(df.shape[0] * train_pct)
train_df = df.iloc[:train_size]
test_df = df.iloc[train_size:]

X_train = train_df.drop(['Close', 'Date'], axis=1)
y_train = train_df['Close']
X_test = test_df.drop(['Close', 'Date'], axis=1)
y_test = test_df['Close']


def CorrectColumnTypes(df):
    for col in df.columns[1:80]:
        df[col] = df[col].astype('float')
    for col in df.columns[-10:]:
        df[col] = df[col].astype('float')
    for col in df.columns[80:-10]:
        df[col] = df[col].astype('category')
    return df

def CreateLags(df,lag_size):
    df, shift = CreateLags(df, lag_size)
    shiftdays = lag_size
    df = df.copy()
    df['Close_lag'] = df['Close'].shift(1)
    return df, shiftdays

def SplitData(df, train_pct, shift):
    X_train, y_train, X_test, y_test, train, test = SplitData(df, train_pct, shift)
    
    train_pt = int(len(df)*train_pct)

    train = df.iloc[:train_pt,:]
    test = df.iloc[train_pt:,:]

    x_train = train.iloc[:shift,1:-1]
    y_train = train['Close_lag'][:shift]
    x_test = test.iloc[:shift,1:-1]
    y_test = test['Close'][:shift]
    
    return x_train, y_train, x_test, y_test, train, test

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)

nn = MLPRegressor(hidden_layer_sizes=(16, 16), max_iter=10000, random_state=42)
nn.fit(X_train, y_train)

y_pred_nn = nn.predict(X_test)
mse_nn = mean_squared_error(y_test, y_pred_nn)


fig = go.Figure()
fig.add_trace(go.Scatter(x=test_df['Date'], y=test_df['Close'], name='Actual'))
fig.add_trace(go.Scatter(x=test_df['Date'], y=y_pred_lr, name=f'LR (MSE={mse_lr:.2f})'))
fig.add_trace(go.Scatter(x=test_df['Date'], y=y_pred_nn, name=f'NN (MSE={mse_nn:.2f})'))
fig.update_layout(height=chart_height, width=chart_width, xaxis=dict(title='Date', tickformat='%Y-%m-%d'),
yaxis=dict(title='Closing Price'))
fig.show()

def LinearRegression_fnc(x_train, y_train, x_test, y_test):
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    lr_pred = lr.predict(x_test)
    lr_MSE = mean_squared_error(y_test, lr_pred)
    lr_R2 = lr.score(x_test, y_test)
    print('Linear Regression R2: {}'.format(lr_R2))
    print('Linear Regression MSE: {}'.format(lr_MSE))
    return lr_pred


def ANN_func(x_train, y_train, x_test, y_test):
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train_scaled = scaler.transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    MLP = MLPRegressor(random_state=1, max_iter=1000, hidden_layer_sizes=(100,),
                        activation='identity', learning_rate='adaptive').fit(x_train_scaled, y_train)
    MLP_pred = MLP.predict(x_test_scaled)
    MLP_MSE = mean_squared_error(y_test, MLP_pred)
    MLP_R2 = MLP.score(x_test_scaled, y_test)
    print('Muli-layer Perceptron R2 Test: {}'.format(MLP_R2))
    print('Multi-layer Perceptron MSE: {}'.format(MLP_MSE))
    return MLP_pred


def CalcProfit(test_df, pred, j):
    pd.set_option('mode.chained_assignment', None)
    test_df['pred'] = np.nan
    test_df['pred'].iloc[:-j] = pred
    test_df['change'] = test_df['Close_lag'] - test_df['Close']
    test_df['change_pred'] = test_df['pred'] - test_df['Close']
    test_df['MadeMoney'] = np.where(test_df['change_pred']/test_df['change'] > 0, 1, -1)
    test_df['profit'] = np.abs(test_df['change']) * test_df['MadeMoney']
    profit_dollars = test_df['profit'].sum()
    print('Would have made: $ ' + str(round(profit_dollars, 1)))
    profit_days = len(test_df[test_df['MadeMoney'] == 1])
    print('Percentage of good trading days: ' + str(round(profit_days/(len(test_df)-j), 2)))
    return test_df, profit_dollars

def PlotModelResults_Plotly(train, test, pred, tickerSymbol, w, h, shift, model_name):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train.index, y=train['Close'], name='Training Data'))
    fig.add_trace(go.Scatter(x=test.index, y=test['Close'], name='Testing Data'))
    fig.add_trace(go.Scatter(x=test.index[shift:], y=pred, name='Model Prediction'))

    fig.update_layout(
        title=tickerSymbol + ' - ' + model_name + ' - ' + str(shift) + ' days shift',
        xaxis_title='Date',
        yaxis_title='Price',
        width=w,
        height=h
    )

    fig.show()

    
for j in shifts:
    print(str(j) + ' days out:')
    print('------------')
    df_lag, shift = CreateLags(df, j)
    df_lag = CorrectColumnTypes(df_lag)
    x_train, y_train, x_test, y_test, train, test = SplitData(df, train_pct, shift)
    print("Linear Regression")
    lr_pred = LinearRegression_fnc(x_train, y_train, x_test, y_test)
    test2, profit_dollars = CalcProfit(test, lr_pred, j)
    PlotModelResults_Plotly (train, test, lr_pred, tickerSymbol, chart_width, chart_height, j, 'Linear Regression')
    print("ANN")
    MLP_pred = ANN_func(x_train, y_train, x_test, y_test)
    test2, profit_dollars = CalcProfit(test, MLP_pred, j)
    PlotModelResults_Plotly (train, test, MLP_pred, tickerSymbol, chart_width, chart_height, j, 'ANN')
    print('------------')



