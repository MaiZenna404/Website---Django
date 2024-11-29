/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html', // Adjust this path based on your project structure
    './dashboard/**/*.html',
    './dashboard/static/css/**/*.css',
  ],
  theme: {
    colors : {
      'beige': '#b8ada3',
      'beige-light': '#f5f5f5',
      'gray-dark': '#273444',
      'gray': '#8492a6',
      'gray-light': '#d3dce6',
      'bordeaux': '#7d2732',
      'bg-gradient': '#a7cdd9',
    },
    fontFamily: {
      sans: ['ui-sans-serif', 'system-ui', 'Helvetica', 'Arial', 'sans-serif'],
      mono: ['ui-monospace', 'SFMono-Regular', 'Courier New', 'monospace'],
    
    },
    extend: {},
  },
  plugins: [],
}

