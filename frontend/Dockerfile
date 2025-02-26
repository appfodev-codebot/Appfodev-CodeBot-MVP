# Use the official Node.js image
FROM node:18

# Set the working directory
WORKDIR /app

# Copy the frontend files
COPY . /app

# Install dependencies and build the app
RUN npm install && npm run build

# Expose the frontend port (default is 3000)
EXPOSE 3000

# Serve the built app using a lightweight server
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
