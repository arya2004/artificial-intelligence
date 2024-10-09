# Use the official SWI-Prolog image from DockerHub
FROM swipl:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Prolog file into the container
COPY main.pl .

# Start SWI-Prolog in interactive mode
CMD ["swipl", "main.pl"]
