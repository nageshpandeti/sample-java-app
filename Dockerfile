# Use Eclipse Temurin JDK 17 base image
FROM eclipse-temurin:17-jdk

# Set working directory
WORKDIR /app

# Copy the built jar from target folder
COPY target/sample-app-1.0.0.jar app.jar

# Expose the application port (optional, helps with Kubernetes Service)
EXPOSE 8080

# Run the jar
ENTRYPOINT ["java", "-jar", "app.jar"]
