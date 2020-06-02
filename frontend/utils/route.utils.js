export const checkRoute = function(route) {
  if (route == 'home') {
    return '/'
  } else if (route && route.includes('--')) {
    route = route.replace('--', '/')
  }
  if (route && !route.startsWith('/')) {
    route = '/' + route
  }
  return route
}
