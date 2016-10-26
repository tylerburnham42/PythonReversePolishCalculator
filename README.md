# Reverse Polish Calculator
This program was written as a code sample for a job. It is a simple python script to evaluate mathematical expressions using Shunting-yard and Reverse Polish Notation.

## Installing  
This application was written in Python 3 using IDLE and the standard library.

## Running the Program
The program accepts the input of a mathematical expression with spaces between the numbers and operations.

```
>>> 3 + 4 * 2 / ( 1 - 5 )
1.0
>>> 3 + 4 * 2 / 1 - 5
6.0
```

##Algorithm 
The program was made by first converting the infix expression to postfix or Reverse Polish Notation using the [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm). 
Then the postfix expression was evaluated using the algorithm found [here](https://en.wikipedia.org/wiki/Reverse_Polish_notation).


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

For the versions available, see the [tags on this repository](https://github.com/tylerburnham42/PythonReversePolishCalculator/tags). 

## Authors

* **Tyler Burnham** - *Initial work* - [tylerburnham42](https://github.com/tylerburnham42)

See also the list of [contributors](https://github.com/tylerburnham42/PythonReversePolishCalculator/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
