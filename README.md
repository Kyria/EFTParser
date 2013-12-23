EFTParser
=========

A python text blocks parser for the famous Eve Online application : Eve Fitting Tool


How to use it
-------------
Just import the class wherever you need it then you need to call the ```parser``` method.

Example :
```python
import eftparser.py
# any code you need 

def parse_eft_textblock_action(eft_textblock):
    parsed_eft = EFTParser.parse(eft_textblock)
    # just do whatever you want with that code

# any other code you need
```

The parsed structure looks like the following :
```yaml
{ 
    ship_type: xxx,
    fit_name: yyy,
    modules: [
        {name: 'module1', charge:'anycharge'},
        {name: 'module without charge', charge: ''},
        ...
    ],
    cargodrones: [
        {name: 'zzz', quantity: 123},
        ...
    ],
}
