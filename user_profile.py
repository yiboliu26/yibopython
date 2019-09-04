def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

def make_sandwich(*make):
    print("Making sandwich with the following materials:")
    for material in make:
        print("- " + material.title())
make_sandwich('pastrami')
make_sandwich('meatball')
make_sandwich('beef')


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('yibo', 'liu', gpa = 4, height = 6, weight = 175)
print(user_profile)

def make_car(make, model, **car_info):
    info = {}
    info['carmake'] = make
    info['carmodel'] = model
    for key, value in car_info.items():
        info[key] = value
    return info
car_profile = make_car('toyota', 'camry', color = 'red', tow_package = True)
print(car_profile)
    