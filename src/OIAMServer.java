import com.sun.net.httpserver.HttpServer;

import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.Random;

public class OIAMServer {
	static final int port=5000;

	public static void main(String args[]) {
		try {
			HttpServer server = HttpServer.create(new InetSocketAddress("0.0.0.0", port), 0);

			server.createContext("/", httpExchange ->
			{
				Random rand = new Random();
				int n = rand.nextInt(1000000) + 1;

				byte response[] = String.valueOf(n).getBytes("UTF-8");

				httpExchange.getResponseHeaders().add("Content-Type", "text/plain; charset=UTF-8");
				httpExchange.sendResponseHeaders(200, response.length);

				OutputStream out = httpExchange.getResponseBody();
				out.write(response);
				out.close();
			});

			server.start();
		} catch (Throwable tr) {
			tr.printStackTrace();
		}
	}
}
