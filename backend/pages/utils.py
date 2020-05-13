import os


class RoutingUtils:

    def __init__(self, path):
        self._path = path

    def get_nuxt_routes(self, nested_path=None):
        from projects.models import Project
        path = nested_path if nested_path else self._path
        routes = []
        for p in os.listdir(path):
            e = os.path.join(path, p)
            if os.path.isdir(e) and not (e.endswith("_slug") or e.endswith("_id")):
                # recursion
                routes.extend(self.get_nuxt_routes(e))
            elif e.endswith("_slug") or e.endswith("_id"):
                routes.extend(self._generate_details_routes(e, Project))
            elif os.path.isfile(e) and e.endswith(".vue"):
                if e.endswith("index.vue"):
                    route = e[:-9].replace(self._path, "")
                    if not route == "/":
                        route = route[:-1]
                else:
                    route = e[:-4].replace(self._path, "")
                route = self._adjust_route(route)
                routes.append(route)
        return routes

    def _generate_details_routes(self, route, _class):
        routes_list = []
        list_name = os.path.basename(os.path.dirname(route))
        if list_name == f"{_class.__name__.lower()}s":
            projects = _class.objects.all()
            routes_list = [
                self._adjust_route(f"/{list_name}/{p.slug_it}") for p in projects
            ]
            routes_list.extend([
                self._adjust_route(f"/{list_name}/{p.slug_en}") for p in projects
            ])
        return routes_list

    def _adjust_route(self, route):
        if route.count("/") > 1:
            count = route.count("/")
            route = route.replace("/", "--")
            route = route.replace("--", "/", count - 1)
        return route


class LayoutUtils:

    def __init__(self, path):
        self._path = path

    def get_layouts(self, nested_path=None):
        path = nested_path if nested_path else self._path
        layouts = []
        for sl in os.listdir(path):
            e = os.path.join(path, sl)
            if os.path.isfile(e) and sl.endswith(".vue"):
                layouts.append(sl[:-4])
            elif os.path.isdir(e):
                layouts.extend(self.get_layouts(e))
        return layouts


if __name__ == "__main__":
    # Test pages
    ru = RoutingUtils("../../frontend/pages")
    routes = ru.get_nuxt_routes()
    print(routes)
    # Test layouts
    lu = LayoutUtils("../../frontend/components/sections")
    layouts = lu.get_layouts()
    print(layouts)
