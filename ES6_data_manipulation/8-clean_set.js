export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string' || !(set instanceof Set)) {
    return '';
  }

  const parts = [];
  set.forEach((value) => {
    if (typeof value === 'string' && value.startsWith(startString)) {
      parts.push(value.slice(startString.length));
    }
  });

  return parts.join('-');
}
