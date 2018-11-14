#include <unistd.h>
#include <stdlib.h>

const char* restart_networking = "systemctl restart networking.service";
const char* stop_networking = "systemctl stop networking.service";
unsigned int seconds = 600;

int main(){
    while(1){
        system(stop_networking);
        sleep(seconds);
        system(restart_networking);
        sleep(seconds);
    }
}
