import matplotlib.pyplot as plt;
import numpy as np;

n = 64;
beta = 0.85;  #Start from this value, doesn't come to the same value
iteration = 150;

directions = {0:np.array([-1,0]), 1:np.array([1,0]), 2:np.array([0,1]), 3:np.array([0,-1])};

#Initialize mesh, only once
mesh0 = np.zeros([n, n]);
mesh1 = np.ones([n, n]);

sum0 = np.zeros(iteration);    #Sum of mesh values
sum1 = np.zeros(iteration);

for iter in range(iteration):

    #For each iteration, sum up Xs
    sum0[iter] = sum(sum(mesh0));
    sum1[iter] = sum(sum(mesh1));

    for i in range(n):
        for j in range(n):

            #Find the neighbors
            #neighbor0 = np.array([0,0,0,0]);  #Store the neighbor values
            #neighbor1 = np.array([0,0,0,0]);  #Set default value =0, so it's fine even if there's no 4 values
            #cnt_valid = 0;  #How many neighbors this site has
            cnt0_same = 0;
            cnt0_diff = 0;
            cnt1_same = 0;
            cnt1_diff = 0;


            for k in range(4):
                try_x = i + directions[k][0];   #New x position
                try_y = j + directions[k][1];   #New y position
                #print try_x, try_y;   This is used to check
                if ((try_x>=0) and (try_x<n) and (try_y>=0) and (try_y<n)):    #if new pos is valid
                    #cnt_valid+=1;   #this is a valid neighbor!

                    #if (mesh0[try_x,try_y] == mesh0[i,j]):       #If equal to center site value, then neighbor = 1
                    if (mesh0[try_x, try_y] == 1):     #This uses count of 1 and 0s
                            #neighbor0[k] = 1;
                            cnt0_same+=1;
                    else:
                            cnt0_diff+=1;

                    #if (mesh1[try_x,try_y] == mesh1[i,j]):
                    if (mesh1[try_x, try_y] == 1):
                            #neighbor1[k] = 1;
                            cnt1_same+=1;
                    else:
                            cnt1_diff+=1;


            #This uses the sum of all probabiities as normalization
            #For each site, compute pi
            #Z = 0;
            #for cc in range(cnt+1):
            #    Z += np.exp(cnt*beta);

            #This uses summation of two factors as normalization
            Z0 = np.exp(cnt0_same*beta)+np.exp(cnt0_diff*beta);
            Z1 = np.exp(cnt1_same*beta)+np.exp(cnt1_diff*beta);

            #pi_0 = np.exp(beta*sum(neighbor0))/Z0;
            #pi_1 = np.exp(beta*sum(neighbor1))/Z1;
            pi_0 = np.exp(beta * cnt0_same) / Z0;
            pi_1 = np.exp(beta * cnt1_same) / Z1;

            #Generate a random variable
            r = np.random.uniform(0,1);

            #Put center site value
            if (pi_0 > r):
                mesh0[i][j] = 1;
            else:
                mesh0[i][j] = 0;

            if (pi_1 > r):
                mesh1[i][j] = 1;
            else:
                mesh1[i][j] = 0;


print sum0;
print sum1;

tao = iteration;   #Coalesed time

for iter in range(iteration-1,-1,-1):
    if (sum0[iter] == sum1[iter]):
        tao = iter;

print mesh0;
print mesh1;

print tao;
x = np.arange(iteration);
plt.plot(x,sum0,'r--',x,sum1,'b--');
plt.show();
