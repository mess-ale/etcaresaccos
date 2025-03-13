// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ['@pinia/nuxt', "@nuxtjs/tailwindcss", '@nuxtjs/google-fonts', '@nuxt/image'],
  compatibilityDate: '2024-04-03',
  googleFonts: {
    families: {
      Oswald: [400, 500, 600, 700], // specify the font weights you need
      Roboto: [400, 500, 700]       // add Roboto with desired weights
    },
    display: 'swap'
  },
  // Other configurations
  devServer: {
    host: '0.0.0.0', // Bind to all network interfaces
    port: 3000,      // Specify the port (default: 3000)
  },
  image: {
    provider: 'ipx', // Default provider for local assets
  },
  app: {
    head: {
      title: 'Etcare SACCOs Ltd',
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/fevicon.ico' },
      ],
    },
  },
})