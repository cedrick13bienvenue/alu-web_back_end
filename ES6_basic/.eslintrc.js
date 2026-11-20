module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
  ],
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  rules: {
    'no-console': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
    'no-underscore-dangle': 'off',
    'no-plusplus': 'off',
    'no-unused-vars': ['error', { argsIgnorePattern: 'res|next|^err' }],
    'max-classes-per-file': 'off',
    'no-shadow': 'off',
    'no-param-reassign': ['error', { props: false }],
  },
};
