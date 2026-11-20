export function uploadPhoto() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        status: 200,
        body: 'photo-profile-1',
      });
    }, Math.floor(Math.random() * 1000));
  });
}

export function createUser() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        firstName: 'Guillaume',
        lastName: 'Salva',
      });
    }, Math.floor(Math.random() * 1000));
  });
}
