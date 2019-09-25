package com.fordgroupfrfr.oiam;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@SuppressWarnings("serial")
@WebServlet(name = "oiam", value = "/" )
public class OiamServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        Random rand = new Random();
        int n = rand.nextInt(1000000)+1;

        PrintWriter out = resp.getWriter();
        out.println(n);
    }
}
