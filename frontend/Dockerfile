FROM node:22-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy project files
COPY . .

# Expose port
EXPOSE 4200

# Start the application with host configured for Docker
CMD ["npm", "start", "--", "--host", "0.0.0.0", "--poll", "2000"]
