import java.util.HashMap;

class ParkingSystem {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

    public ParkingSystem(int big, int medium, int small) {
        map.put(1, big);
        map.put(2, medium);
        map.put(3, small);
    }

    public boolean addCar(int carType) {
        if (map.get(carType) > 0) {
            map.put(carType, map.get(carType) - 1);
            return true;
        } else {
            return false;
        }
    }
}