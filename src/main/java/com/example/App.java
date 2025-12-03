package com.example;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello, Kubernetes! Application is running.");
        
        // Keep the app alive so the container doesn’t exit immediately
        while (true) {
            try {
                Thread.sleep(60000); // sleep 1 minute
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
