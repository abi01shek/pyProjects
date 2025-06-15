import py4j.GatewayServer;
import org.rumbledb.api.Rumble;
import org.rumbledb.config.RumbleRuntimeConfiguration;

public class RumbleEntryPoint {
    private Rumble rumble;
    private RumbleRuntimeConfiguration configuration;

    public RumbleEntryPoint() {
        String[] args = {"run", "-q", "'1+1'"};
        configuration = new RumbleRuntimeConfiguration(args);
        rumble = new Rumble(this.configuration);
    }

    public Rumble getRumble(){
        return rumble;
    }

    public static void main(String[] args){
        GatewayServer gatewayServer = new GatewayServer(new RumbleEntryPoint());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }

}
