{
    "targets": [
        {
            "target_name": "natasha2",
            "sources": [ 
                "src/main.cpp", "src/libnatasha2.cpp",

                "src/natasha2/libfortuna/blf.c", "src/natasha2/libfortuna/fortuna.c", "src/natasha2/libfortuna/internal.c", "src/natasha2/libfortuna/md5.c", 
                "src/natasha2/libfortuna/px.c", "src/natasha2/libfortuna/random.c", "src/natasha2/libfortuna/rijndael.c", "src/natasha2/libfortuna/sha1.c", 
                "src/natasha2/libfortuna/sha2.c",

                "src/natasha2/src/csvfile.cpp", "src/natasha2/src/fortuna.cpp", "src/natasha2/src/game3x5.cpp", "src/natasha2/src/gamelogic.cpp", 
                "src/natasha2/src/staticcascadingreels3x5.cpp", "src/natasha2/src/symbolblock2.cpp", "src/natasha2/src/utils.cpp", 
                
                "src/natasha2/protoc/base.pb.cc", "src/natasha2/protoc/tlod.pb.cc", 
                
                "src/natasha2/tlod/tlod.cpp"
                ],
            "include_dirs" : [
 	 			"<!(node -e \"require('nan')\")"
			]
        }
    ],
}