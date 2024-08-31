# What is Analysis?

The analysis of an algorithm provides background information that gives us a general idea of how long an algorithm will take for a given problem set.

For each algorithm considered, we will come up with an estimate of how long it will take to solve a problem that has a set of *N* input values.

```
largest = a
if b > largest then
    largest = b
end if
if c > largest then
    largest = c
end if
if d > largest then
    largest = d
end if
return largest
```

```
if a > b then
    if a > c then
        if a > d then
            return a
        else
            return d
        end if
    else
        if c > d then
            return c
        else
            return d
        end if
    end if
else
    if b > c then
        if b > d then
            return b
        else
            return d
        end if
    else
        if c > d then
            return c
        else
            return d
        end if
    end if
end if
```

These two algorithms, each one will do exactly three comparisons to find the answer. In terms of time, these two algorithms are the same, but in terms of space, the first needs more because of the temporary variable called *largest*.

### Purpose of Determining `time` and `space`

- The purpose of deteriminig these values is, to use them to compare how efficiently two different algorithms solve a problem.

- The purpose of analysis of algorithms is not to give formula that will tell us exactly how many seconds or computer cycles a particular algorithm will take.