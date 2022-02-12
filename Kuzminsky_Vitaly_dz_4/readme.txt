Приветствую Анатолий!
Катастрофически отстаю, не успеваю качественно разобраться в материале.
Поэтому только основные задания на проверку, в голове вертятся примерные решения со *, но время неумолимо.
Вопросы:
1. Почему в функциях "currency_rates" PyCharm мне подсвечивает первый "return".
Он, конечно, дал мне подсказку, но я не очень разобрался.
Он ругается, что "return" пустой - и вынужден отдавать None - на это?
The return statement
return_stmt ::=  "return" [expression_list]
return may only occur syntactically nested in a function definition, not within a nested class definition.
If an expression list is present, it is evaluated, else None is substituted.
return leaves the current function call with the expression list (or None) as return value.
When return passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the function.
In a generator function, the return statement indicates that the generator is done and will cause StopIteration to be raised. The returned value (if any) is used as an argument to construct StopIteration and becomes the StopIteration.value attribute.

2. Тоже PyCharm мне подсвечивает "code" в "utils.py"
Cannot find reference 'code' in 'sys.pyi'
No documentation found.
Так да, "code" приходит внешний при вызове модуля "utils" и в самом "utils.py" его нет.
Верно рассуждаю или ошибочно?
И почему ищет в "sys.pyi"?
Я почитал про "".pyi файлы - это стабы (stubs). Их назначение - предоставлять информацию о типизации кода."
Пока звучит не очень =)