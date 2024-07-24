# Use the official Rasa SDK image as base
FROM rasa/rasa-sdk:latest

# Copy actions directory to working directory
COPY ./actions /app/actions

# Install dependencies
RUN pip install -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Expose the Rasa actions server port
EXPOSE 5055

# Start the Rasa actions server
CMD ["start", "--actions", "actions"]
