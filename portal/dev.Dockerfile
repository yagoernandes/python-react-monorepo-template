FROM node:14

WORKDIR /usr/src/app/portal

COPY package*.json ./

RUN yarn install --immutable --immutable-cache --check-cache

EXPOSE 3080

CMD ["yarn", "dev"]