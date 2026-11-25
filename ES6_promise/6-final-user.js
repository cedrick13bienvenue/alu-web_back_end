import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function settle(promise) {
  return promise
    .then((value) => ({ status: 'fulfilled', value }))
    .catch((error) => ({ status: 'rejected', value: error }));
}

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    settle(signUpUser(firstName, lastName)),
    settle(uploadPhoto(fileName)),
  ]);
}
