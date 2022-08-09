s="aRTificial INTELLIgence"
def test(ch):
switcher={
    case 1:
           print(s.upper())
    case 2:
           print(s.lower())
    case 3:
           print(s.isupper())
    case 4:
           print(s.islower())
    case 5:
           print(s.replace('INTELLIgence','Neural NEtwork',1))
    case 6:
           print(s.startswith("T"))
    case 7:
           print(s.endswith("e"))
    case 8:
           print(s.capitalize())
    case 9:
           print(s.swapcase())
    default:
        exit

};
int main()
{
    ch=int(input("num"))
}
