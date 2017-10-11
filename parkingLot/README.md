# Automated ticketing system for Parking lot 


###### The code is written in Python 

parking_lot.sh shell script triggers the python script, Or we can directly execute python script 

Sample execution formats
```
./parking_lot.sh
./parking_lot.sh file_inputs.txt

python parking_lot.py file_inputs.txt
python parking_lot.py

```



Possible Inputs
```
create_parking_lot 6
park KA-01-HH-1234 White
park KA-01-HH-9999 White
park KA-01-BB-0001 Black
park KA-01-HH-7777 Red
park KA-01-HH-2701 Blue
park KA-01-HH-3141 Black
leave 4
status
park KA-01-P-333 White
park DL-12-AA-9999 White
registration_numbers_for_cars_with_colour White
slot_numbers_for_cars_with_colour White
slot_number_for_registration_number KA-01-HH-3141
slot_number_for_registration_number MH-04-AY-1111
exit
```


Test cases are available in test.py

Command for Test case execution:
```
python test.py

```
