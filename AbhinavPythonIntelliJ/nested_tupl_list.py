albums=["welcome to my nightmare","alice cooper",1975,
"bad company","bad company",1974,
"nightflight","budgie",1981,
"more mayhem","emilda may",2011,
"ride the lighting","metallica",1984
]

print(len(albums))

albums=[("welcome to my nightmare","alice cooper",1975),
("bad company","bad company",1974),
("nightflight","budgie",1981),
("more mayhem","emilda may",2011),
("ride the lighting","metallica",1984)
]

# for album in albums:
#     name,artist,year=album
#     print(f"name:{name} ,artist:{artist} ,year:{year}")
#     print()

for name,artist,year in albums:
#     name,artist,year=album
    print(f"name:{name} ,artist:{artist} ,year:{year}")
    print()