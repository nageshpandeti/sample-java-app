FROM eclipse-temurin:17-jdk
WORKDIR /app
COPY target/sample-app-1.0.0.jar app.jar
ENTRYPOINT ["java", "-cp", "app.jar", "com.example.App"]
