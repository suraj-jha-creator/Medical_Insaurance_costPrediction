import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
ans=0.0
def cost(val):
    window = Tk()
    window.title("Insurance Cost Detection")
    window.geometry('500x100')
    x = Label(window ,text = "The cost is").grid(row = 0,column = 0)
    y=Label(window ,text = val).grid(row = 0,column = 1)
    window.mainloop()




def crvs():
    df = pd.read_csv("insurance.csv")
    plt.figure(figsize=(5,5))
    cr=sns.barplot(x='region', y='charges', data=df)
    plt.title('Cost vs Region')
    plt.show()

def csvs():
    df = pd.read_csv("insurance.csv")
    plt.figure(figsize=(5,5))
    sns.barplot(x='sex', y='charges',hue='smoker', data='df')
    plt.title('Charges for smokers')
    plt.show()
   
   


def gender():
    df = pd.read_csv("insurance.csv")

    df.head()

    df.shape

    df.info()

    df.isnull().sum()


    df.columns

    df.describe()


    plt.figure(figsize=(5,5))
    style.use('ggplot')
    sns.countplot(x='sex', data=df)
    plt.title('Gender Distribution')
    plt.show()
    
def smoker():
    df = pd.read_csv("insurance.csv")

    df.head()

    df.shape

    df.info()

    df.isnull().sum()


    df.columns

    df.describe()

    plt.figure(figsize=(5,5))
    sns.countplot(x='smoker', data=df)
    plt.title('Smoker')
    plt.show()


def region():
    df = pd.read_csv("insurance.csv")

    df.head()

    df.shape

    df.info()

    df.isnull().sum()


    df.columns

    df.describe()
    plt.figure(figsize=(5,5))
    sns.countplot(x='region', data=df)
    plt.title('Region')
    plt.show()


def clicked():
    df = pd.read_csv("insurance.csv")

    df.head()

    df.shape

    df.info()

    df.isnull().sum()


    df.columns

    df.describe()

    # plt.figure(figsize=(5,5))
    # style.use('ggplot')
    # sns.countplot(x='sex', data=df)
    # plt.title('Gender Distribution')
    # plt.show()


    # plt.figure(figsize=(5,5))
    # sns.countplot(x='smoker', data=df)
    # plt.title('Smoker')
    # plt.show()

    # plt.figure(figsize=(5,5))
    # sns.countplot(x='region', data=df)
    # plt.title('Region')
    # plt.show()


    # plt.figure(figsize=(5,5))
    # sns.barplot(x='region', y='charges', data=df)
    # plt.title('Cost vs Region')


    # plt.figure(figsize=(5,5))
    # sns.barplot(x='sex', y='charges',hue='smoker', data=df)
    # plt.title('Charges for smokers')

    # fig, axes = plt.subplots(1,3, figsize=(15,5), sharey=True)
    # fig.suptitle('Visualizing categorical columns')
    # sns.boxenplot(x='smoker', y= 'charges', data=df, ax=axes[0])
    # sns.boxenplot(x='sex', y= 'charges', data=df, ax=axes[1])
    # sns.boxenplot(x='region', y= 'charges', data=df, ax=axes[2])

    # df[['age','bmi','children','charges']].hist(bins=30, figsize=(10,10), color='blue')
    # plt.show()

    df.head()


    df['sex'] = df['sex'].apply({'male':0, 'female':1}.get)
    df['smoker'] = df['smoker'].apply({'yes':1, 'no':0}.get)
    df['region'] = df['region'].apply({'southwest':1, 'southeast':2, 'northwest':3, 'northeast':4}.get)


    # In[21]:


    df.head()


    # In[22]:


    plt.figure(figsize=(10,7))
    sns.heatmap(df.corr(), annot = True)
    plt.show()


    # In[23]:


    X = df.drop(['charges', 'sex'], axis=1)
    y = df.charges


    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)


    linreg = LinearRegression()

    linreg.fit(X_train, y_train)
    pred = linreg.predict(X_test)


    plt.scatter(y_test, pred)
    plt.xlabel('Y test')
    plt.ylabel('Y pred')
    plt.show()

    age=int(aa.get())
    bmi=int(bb.get())
    smoker=int(smoke.get())
    children=int(cc.get())
    region=int(reg.get())

    data = {'age':age, 'bmi':bmi, 'children':children, 'smoker':smoker, 'region':region}
    index = [0]
    cust_df = pd.DataFrame(data, index)
    cust_df


    cost_pred = linreg.predict(cust_df)
    cost(linreg.predict(cust_df))
    print("The medical insurance cost of the new customer is: ", cost_pred)



from tkinter import *
from tkinter import ttk
window_1 = Tk()
window_1.title("Insurance Cost Detection_1")

window_1.geometry('600x450')
#    data = {'age':age, 'bmi':bmi, 'children':chi, 'smoker':sm, 'region':reg}
# window.configure(background = "grey")

aa = StringVar()
bb = StringVar()
cc=StringVar()
smoke = StringVar()
reg=StringVar()


a = Label(window_1 ,text = "Age").grid(row = 0,column = 0)
#align the text
b = Label(window_1 ,text = "BMI").grid(row = 1,column = 0)
#align the text
c = Label(window_1 ,text = "Children").grid(row = 2,column = 0)
#align the text
d = Label(window_1 ,text = "Enter \n1 If Smoker \n0 If Not Smoker").grid(row = 3,column = 0)
#align the text
f = Label(window_1 ,text = "Enter Region \n1.SouthWest\t2.SouthEast\n\n3.NorthWest\t4.NorthEast").grid(row = 4,column = 0)
#align the text

a1 = Entry(window_1,textvariable=aa,).grid(row = 0,column = 1)
#input box increase size
b1 = Entry(window_1,textvariable=bb).grid(row = 1,column = 1)
#input box increase size
c1 = Entry(window_1,textvariable=cc).grid(row = 2,column = 1)
#input box increase size
d1 = Entry(window_1,textvariable=smoke).grid(row = 3,column = 1)
#input box increase size
d1 = Entry(window_1,textvariable=reg).grid(row = 4,column = 1)
#input box increase size



btn = ttk.Button(window_1 ,text="Submit",command=clicked).grid(row=6,column=4)

btn_1= ttk.Button(window_1 ,text="Gender Distribution",command=gender).grid(row=0,column=4)
btn_2= ttk.Button(window_1 ,text="Smoker",command=smoker).grid(row=2,column=4)
btn_3= ttk.Button(window_1 ,text="Region",command=region).grid(row=3,column=4)
btn_4= ttk.Button(window_1 ,text="Cost Vs Region",command=crvs).grid(row=4,column=4)
btn_5= ttk.Button(window_1 ,text="Charges for smokers",command=csvs).grid(row=5,column=4)
# btn_5= ttk.Button(window_1 ,text="",command=last).grid(row=6,column=2)


window_1.mainloop()





