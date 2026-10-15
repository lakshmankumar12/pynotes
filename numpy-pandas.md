# pandas

* series - one column's data -- always of one dtype
    * built on numpy array
* dataframe - one 2-D data
    * several series sharing common row index



```python
## read from file
df = pd.read_excel("filename.xlsx")
df = pd.read_csv("filename.csv")


## loc slices are inclusive of begin and end
## masks work on loc.
df.loc["row_label", "col_label"]

## iloc slices behave like regular py slices
df.iloc[row_position, col_position]

## set this column as the per-row index
new_dataframe = a.set_index("col_name")

## get one column
df['one_col']
df[['col1','col2']]  ## mutli columsn as passes as [ [list] ]

## also using loc
df.loc[:, 'one_col']
df.loc[:, ['col1', 'col2']]

```

## useful functions

```python
dataframe.shape    ## is a property -- is a tuple
dataframe.dtypes   ## is a property - gives the type of each column. (is a series)
dataframe.head(n)  ## default = 5
dataframe.tail(n)  ## default = 5
dataframe.info()   ## prints general detail on all columns, returns None!
dataframe.describe() ## give details only on numeric column, return the information

len(dataframe)     ## gives num rows

## sorting -- the index travels with the sorted rows.. so .loc[old_index] will give the same row, but iloc[n] can be diff!!
dataframe.sort_values(by=["col1","col2"], ascending=[False, False])

## get nulls -- give another df that is of the same size
df.isnull()
df.isna()  ## exact alias of isnull()
df.notnull()
df.notna()  ## exact alias of notnull()

## get counts of nulls - one entry per column.
df.isnull().sum()
## get counts of all nulls in the df
df.isnull().sum().sum()
## get a bool per column
raw_students.isnull().any()

## drop null values , by default drops rows. axis=1, drops columns
df.dropna()
df.dropna(axis=1)

## fill with a said value
value = df[column_name].mean()
newdf = df[column_name].fillna(value)

## duplicated -- gives True if a row is a dup of another row. First row is False, the further ones are True
df.duplicated()
## check only select columns
df.duplicated(subset=["colname1","colname2"])
## remove duplicates
newdf = df.drop_duplicates()

## get unique values
df[colname].unique()

## .str.next_func() -- apply next_func() on every item on the given column
df[new_col] = df[col].str.strip().str.title()

## convert
df[new_col] = df[col].astype(int)
## overwrites same col
df[col] = df[col].astype(int)

list_var = df[col].tolist()

## grouping

### .groupby("col") shrinks the df into as many rows as there are distinct values in "col"
df.groupby(["col1", "col2"])["value_col_name"].agg_fn()

## rows that have NaN values on the "grouping" column are DROPed !!
## groupby(..., dropna=False)
## groupby(..., as_index=False) ## .. see below

## eg  agg_fn() - min(), max(), sum(), mean(), count()
df.groupby("city")["amount"].sum()            ## equivlent SQL: SELECT city, SUM(amount) FROM orders GROUP BY city;
df.groupby("city")["amount"].agg(["sum", "mean", "max", "min", "count"])

g  = df.groupby(["col1", "col2"])     # DataFrameGroupBy object
sg = g["value_col_name"]              # SeriesGroupBy  (single column via [] with a string)
r  = sg.sum()                         # Series, indexed by a MultiIndex of (col1, col2)

## What groupby does to the index:
##     When you aggregate, the group keys become the index of the result.
##     With two keys, each row label is a tuple of (col1, col2). That’s a MultiIndex, which is a hierarchical index with multiple levels

r.reset_index()  ## converts the Index()/MultiIndex() into column(s) again

## get a new df directly w/o bothering with intermediate groupby objects
newdf = df.groupby(["col1", "col2"], as_index=False)["value"].sum()

## merging

## same as SQL -- JOIN

left_df.merge(right_df, on="shared_col_name", how="inner")      ## how = one of inner/left/right/outer/cross  (cross is similar to outer without any on)
## when the 2 dfs has diff col-names -- the result gets both the cols
left_df.merge(right_df, left_on="col_name_on_left", right_on="col_name_on_right", how="inner")

## we always merge first -- get the new df , and the group-by after it.. Same as SQL order.

## if the col exist with same name on both sides, but isn't called out on the on=[..], then the appear as col_x/col_y .. control this with suffixes=("_left","_right")


## correlation matrix
corr_matrix = df[["col1", "col2"]].corr()

```

# numpy

* array is the basic datatype
    * has a `a.shape` - gives a tuple. Each entry size of that dimensions. Lenght of tuple indicates how many dimensions there are
    * has a `a.dtype` - give the dataypte of each member. All members across all dimentions are the same. This is why numpy ararys are faster.
    * note that the above are properties (not methods)

* arithmetic operators give new arrays
* masks - give booleans of the same size for the given expression
    * array[mask] .. gives a new array (not a view)


```python
## basic array

# from a list
a = np.array([1,2,3])

# from a range
a = np.arange(1,13).reshape(3,4)

```

## indexing

```python

a[1, 2]        # single element -> 7
a[0]           # first row -> [1 2 3 4]
a[:, 1]        # second column -> [ 2  6 10]
a[0:2, 1:3]    # rows 0-1, cols 1-2 -> [[2 3], [6 7]]
a[:, -1]       # last column -> [ 4  8 12]
a[::2, ::2]    # every other row & col -> [[ 1  3], [ 9 11]]
a[::-1]        # rows reversed
a[:, ::-1]     # columns reversed

```

* views vs copies
    * basic slices give a view

```python
b = a[0:2, 0:2]
b[0, 0] = 99   # a[0, 0] is now 99 too
c = a[0:2, 0:2].copy()  # independent copy

np.shares_memory(a, v)   # True
v.base is a              # True for a direct view

```

* arithmetic operatos give a new copy

* sum on axis
    * A good way to remember it is through the shape: the axis you pass disappears.

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])     # shape (2, 3)

a.sum(axis=0)   # [5 7 9]    -> 1+4, 2+5, 3+6   shape (3,)
a.sum(axis=1)   # [ 6 15]    -> 1+2+3, 4+5+6    shape (2,)
a.sum()         # 21         -> everything

```

## some basic ops

```python

a.reshape(1,2)   ## total elems before and after should match
a.flatten()      ## gives a 1D array
a.T              ## transpose of .. notice its a member. its a view

```

### summng with axis

```python

a.sum(axis=2)

```



## broadcasting rules

Broadcasting allowing arrays of different shapes to combine in operations when dimensions are compatible.

Compatibility Rules: When combining arrays, compare shapes from right to left:
* Dimensions must be equal, OR
* One of the dimensions must be 1, OR
* Missing dimensions are treated as 1

```python

[[1,2,3],[4,5,6]] + 5 ## (2,3) + scaler = ok
[[1,2,3],[4,5,6]] + [10,20,30] ## (2,3) + (3,) = ok .. right to left 3=3, 2=missing okay
[[1,2,3],[4,5,6]] + [[10,20,30],[40,50,60]] ## (2,3) + (2,3) = ok .. right to left 3=3, 2=2 okay
[[1,2,3],[4,5,6]] + [[1],[2]] ## (2,3) + (2,1) = ok .. right to left 3=1(matches one), 2=2 okay

[[1,2,3],[4,5,6]] + [10,20] ## (2,3) + (2,) = NOT OKAY.. right to left 3!=2

```


# matplotlib

* figure - entire canvas
* axis   - on chart on that figure


```python
import matplotlib.pyplot as plt


## create a new figure with one axis
fig, ax = plt.subplots()

## set the data for x-axis and y-axis for that axis as a line-graph
ax.plot(sales["month"], sales["revenue"])
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.set_title("Month on Month Revenue")

# 2 lines on same axis
ax.plot(sales["month"], sales["revenue"], label="...", marker="o", color="tab:brown", linestyle="--")
ax.plot(sales["month"], sales["costs"], label="...", marker="x", color="tab:green")
ax.legend()

## render the figure
plt.show()

## save to a file
plt.savefig("revenue_chart.png", dpi=300)

```

** supported tableu colors:

```
tab:blue            #1f77b4
tab:orange          #ff7f0e
tab:green
#2ca02c
tab:red
#d62728
tab:purple
#9467bd
tab:brown
#8c564b
tab:pink
#e377c2
tab:gray
#7f7f7f
tab:olive 
#bcbd22
tab:cyan

```


* multiple

```
## create a new figure with one axis
fig, axes = plt.subplots(2,3)
axes[0,2].plot(x_values, y_values)
```

* diff types

```python
ax.plot(x_values, y_values)
ax.bar(x_values, y_values)
ax.scatter(x_values, y_values)

```

* seaborn

```python

import matplotlib.pyplot as plt
import seaborn as sns

# it will start from first and take so many bins
# each bin includes lower-value/excludes higher value, except last-bin, which includes that value!!
sns.histplot(data=df, x="column", bins=[50, 60, 70, 80, 90, 100])
# split the range into n bins
sns.histplot(data=df, x="column", bins=10)


sns.boxplot(data=raw_students, x="city", y="math_score")

sns.heatmap(corr_matrix, annot=True, cmap="blue")

plt.show()

```



