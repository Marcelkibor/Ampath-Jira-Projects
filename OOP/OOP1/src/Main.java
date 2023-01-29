public class Main {
    public static void main(String[] args) throws Exception {
        // test inheritance
        Bmw bmw1 = new Bmw();
        System.out.println("bmw1 production year is->"+bmw1.getProductionYear());       

        // test polymorphism
        Car toyota1 = new Toyota(50);
        System.out.println("toyota1 maximum speed is->"+toyota1.getMaximumSpeed());

        // test abstraction
        Mercedes mercedes1 = new Mercedes();
        mercedes1.setAcceleration(10, 2); 
        System.out.println("mercedes1 acceleration is->"+ mercedes1.getAcceleration());

        //test encapsulation
        Nissan nissan1 = new Nissan();
        nissan1.setWindowColor("Transparent");
        System.out.println("nissan1 Window color is->"+nissan1.getWindowColor());

    }
}
