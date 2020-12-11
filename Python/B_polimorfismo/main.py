from a import A
from b import B
from c import C

def main():
    c = C() #Soy de la clase C
    c.a() #Este método lo heredo de A
    c.b() #Este método lo heredo de B
    c.c() #Este método es de C

if __name__ == "__main__":
    main()