FROM openjdk:17-jdk-slim-bullseye
COPY target/sample-java-app-1.0-SNAPSHOT.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
