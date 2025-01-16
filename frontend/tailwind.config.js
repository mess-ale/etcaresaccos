/** @type {import('tailwindcss').Config} */
export default {
    content: [],
    theme: {
      extend: {},
    },
    plugins: [],
  }
  
  module.exports = {
    theme: {
      extend: {
        colors: {
          primary: '#214080',
          secondary: '#D92A27',
          background: '#EEF4FF',
          white: '#fff',
          black: '#000',
        },
        fontFamily: {
          oswald: ['Oswald', 'sans-serif'],
          roboto: ['Roboto', 'sans-serif'],
        },
        fontSize: {
          'xxs': '0.6rem',
          'xs': '0.75rem',
          'sm': '0.875rem',
          'base': '1rem',
          'lg': '1.125rem',
          'xl': '1.25rem',
          '2xl': '1.5rem',
          '3xl': '1.875rem',
          '4xl': '2.25rem',
          '5xl': '3rem',
          '6xl': '4rem',
        },
        spacing: {
          '1/2': '0.125rem',
          '1': '0.25rem',
          '2': '0.5rem',
          '3': '0.75rem',
          '4': '1rem',
          '5': '1.25rem',
          '6': '1.5rem',
          '8': '2rem',
          '10': '2.5rem',
          '12': '3rem',
          '16': '4rem',
          '20': '5rem',
          '24': '6rem',
          '32': '8rem',
          '34': '14rem',
        },
        screens: {
          xxxs: '120px',  // Extra small devices (e.g., small phones)
          xs: '320px',  // Extra small devices (e.g., small phones)
          sm: '480px',  // Small devices (e.g., smartphones)
          md: '768px',  // Medium devices (e.g., tablets in portrait mode)
          lg: '1024px', // Large devices (e.g., tablets in landscape or small laptops)
          xl: '1280px', // Extra-large devices (e.g., laptops, desktops)
          // xxl: '1440px', // 2XL devices (e.g., large desktops)
          // xxxl: '1920px', // Ultra-wide screens
        },
      },
    },
  };