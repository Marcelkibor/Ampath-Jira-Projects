public class Mercedes  implements AccelerationInterface{
    private float acceleration;
    
    @Override
    public  void setAcceleration(float changeInAcceleration, float changeInVelocity) {
        acceleration = changeInAcceleration/changeInVelocity;
    
    }
    @Override
    public float getAcceleration(){
        return acceleration;
    }
}
