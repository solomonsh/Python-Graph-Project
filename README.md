# Comedians in _Graphs_ Getting Coffee

In this exercise you will work with graphs trying to answer questions about standup 
comedians.

<img src="https://media.giphy.com/media/3oEjI44vogVayGlOqQ/giphy.gif" align=right/>

## Exercise 1. _Getting the data._

**3 points**

The data is in CSV format, in the `comedians.csv` file.  This CSV has two
columns, `source` and `target`, and it represents the influences a comedian has
had.  For example, a csv like:

```
source, target
Steve Martin, Pepe
```

would indicate that Steve Martin influenced Pepe.

In this exercise you will need to implement the `parse_csv_to_graph` function
from the `comedians.py` file.  It should receive the path of the CSV and return
the graph of comedian influences represented as adjacency lists.

You can represent the graph as we did in class, using plain dictionaries, or
you can model the graph using classes, for example.

The function must control all errors that happen inside and return `None` in
case any occur.

## Exercise 2.  _Influence chains._

**2 points**

In this exercise you will need to search influence chains in your graph.  You
will need to implement the `influence_chains` function in the `comedians.py`
file.

It is acceptable for this exercise to consider that a comedian has influenced
themself.

As you can see in the signature of `influence_chains` function, it
receives a mandatory parameter `start` and another optional one `end`.
When this function receives only one, it should return a dictionary
with all the comedians for which the first comedian has been an
influence.  When receiving both parameters, it should just return the
_comedy path_ between two comedians.

## Exercise 3.  _Top 10 influencers_

**2 points**

Implement the `top_10_influencers` function, and make it return a list with the
top 10 most influential comedians in the graph.

## Exercise 4.  _Printing the graph_

**1 point**

For this exercise you will need to represent the data in the graph in
a visual way.  You can try to do it by printing the data in a nice
way, or you can try using a library that supports printing graphs.

In case you will end up using a library, you can take a look at
https://networkx.org, a library included in Anaconda that's great for
studying networks and graphs.

# Due date

This exercise is due on **2021-12-20, at 22:00 (Madrid time)**.  I will only correct the last in Github.

# Evaluation method

Maximum possible points: **10**

| Area                 |       Points |
| :------------------- | -----------: |
| Exercise 1           | **3 points** |
| Exercise 2           | **2 points** |
| Exercise 3           | **2 points** |
| Exercise 4           | **1 points** |
| General coding style | **2 points** |


# Attributions

The data and the idea comes from [this beautiful map](https://www.reddit.com/r/dataisbeautiful/comments/bp0oqq/i_spent_seven_months_researching_the_comic/).
