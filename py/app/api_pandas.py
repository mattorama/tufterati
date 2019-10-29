#%%
import numpy as np
import pandas as pd

#%%
s = pd.Series([1, 3, 5, np.nan, 6, 8])

#%%
dates = pd.date_range('20130101', periods=6)

#%%
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
#%%
df.index

#%%
df.sort_index(axis=1, ascending=False)

#%%
df.sort_values(by='B')

#%%
df.loc[dates[0]]

#%%
df.loc['20130102':'20130104', ['A', 'B']]

#%%
df.at[dates[0], 'A']

#%%
df.iloc[3:5, 0:2]

#%%
df.iat[1, 1]

#%%
df[df.A > 0]

#%%
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
df['F'] = s1

#%%
df.loc[:, 'D'] = np.array([5] * len(df))
df

#%%
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
df1

#%%
help(s.shift)
#%%
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)

#%%
s.shift(2)

#%%
df.apply(np.cumsum)

#%%
df.apply(lambda x: x.max() - x.min())

#%%
s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()

#%%
pd.concat([df[:3], df[3:7]])

#%%
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
s = df.iloc[3]
df.append(s, ignore_index=True)

#%% split-apply-combine
#%%
tuples = list(zip(*[
    ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
   ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
stacked = df.stack()
stacked

#%%
stacked.unstack()

#%%
stacked.unstack(1)

#%%
stacked.unstack([0,1])

#%%
rng = pd.date_range('1/1/2012', periods=100, freq='S')

#%%
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

#%%
ts.resample('1Min').sum()

#%%
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
df["grade"] = df["raw_grade"].astype("category")
df["grade"].cat.categories = ["very good", "good", "very bad"]

#%%
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
df.groupby("grade").size()

#%%
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2020', periods=1000))
ts = ts.cumsum()
ts.plot()

#%%
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.plot()

#%%
df.index.array

#%%
df.A.array

#%%
