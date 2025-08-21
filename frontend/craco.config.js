module.exports = {
  devServer: {
    allowedHosts: 'all',
    host: 'localhost',
    port: 3000,
    client: {
      webSocketURL: {
        hostname: 'localhost',
        pathname: '/ws',
        port: 3000,
        protocol: 'ws',
      },
    },
  },
};
