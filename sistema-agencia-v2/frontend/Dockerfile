
FROM node:18 as build
WORKDIR /app
COPY package*.json ./
RUN npm install

RUN npm install bootstrap@5.3.2 @popperjs/core --save
RUN npm install sweetalert2 just-validate chart.js --save
COPY . .
RUN npm run build -- --configuration production

FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]