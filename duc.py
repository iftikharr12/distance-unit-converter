import streamlit as st

def distance_converter (value, from_unit, to_unit):
    if from_unit == "km":
        meter = value * 1000
    elif from_unit == "m":
        meter = value
    elif from_unit == "cm":
        meter = value / 100
    elif from_unit == "mm":
        meter = value / 1000
    else:
         print("worng_unit")
         return None

    if to_unit == "km":
            result = meter / 1000
    elif to_unit == "m":
        result = meter 
    elif to_unit == "cm":
        result = meter * 100
    elif to_unit == "mm":
        result = meter * 1000
    else:
        print("worng_unit")
        return None
    return result

def main():
    st.title("Distance_Converter")
    st.header("Select your unit and put your value")
    st.write("Available units: km, m, cm, mm")
    from_unit = st.text_input("Enter unit from")
    to_unit = st.text_input("Enter unit to")
    value = st.number_input("Enter your value", min_value=0)
    if st.button("Convert"):
        result  = distance_converter (value, from_unit, to_unit)
        st.write("Convert Value is :", result)


    #print("Available units: km, m, cm, mm")

    #from_unit = input("convert from: ")
    #to_unit = input("conver to: ")


    #try:
        #value = float(input("enter the number"))
    #except:
        #print("enter correct number")
        #return 

    #result  = distance_converter (value, from_unit, to_unit)
    #if result is not None:
        #print(f"\n{value} {from_unit}, is equal to {result} {to_unit}")

main()

    


