function show_q (Ts, T, q_right_leg_rad, q_left_leg_rad, q_right_arm_rad, q_left_arm_rad)
%
% This function shows the join trajectory of arms and legs of a humanoid robot.
% It has the join limits of the humanoid robot HOAP-3.
%
%time vector
time=0:Ts:T-Ts;

% Check if t is a row or a column vector
n_elements = length(time);
if (length(q_right_leg_rad) ~= n_elements)
  error('Trajectory and time must have the same lenght');
end
q_right_leg_rad = trajectoriesToColumns(q_right_leg_rad);
q_left_leg_rad = trajectoriesToColumns(q_left_leg_rad);
q_right_arm_rad = trajectoriesToColumns(q_right_arm_rad);
q_left_arm_rad = trajectoriesToColumns(q_left_arm_rad);

%links positions range
q_right_m = [-91; -31; -71; -1; -61; -25];
q_right_M = [31; 21; 82; 130; 61; 25];
q_left_m = [-31; -21; -82; -130; -61; -25];
q_left_M = [91; 31; 71; 1; 61; 25];
range_q_right = [q_right_m, q_right_M];
range_q_left = [q_left_m, q_left_M];

q_right_leg = 180/pi.*q_right_leg_rad;
q_left_leg = 180/pi.*q_left_leg_rad;
q_right_arm = 180/pi.*q_right_arm_rad;
q_left_arm = 180/pi.*q_left_arm_rad;

%right leg links positions plot
figure('Name','Right leg links positions','NumberTitle','off')
for ii=1:6
    subplot(2,3,ii);
    hold on
    plot(time,q_right_leg(:,ii),'b');
    plot(time,range_q_right(ii,:)'*ones(1,length(time)),'r')
    xlim([0 (T-Ts)]);
    title(['\theta_',num2str(ii)])
    if min(q_right_leg(:,ii))<range_q_right(ii,1) || max(q_right_leg(:,ii))>range_q_right(ii,2)
        title(['OUT OF RANGE!!!: \theta_',num2str(ii)]);
    end
    xlabel('time (s)')
    ylabel('Position (deg)')
end

%left leg links positions plot
figure('Name','Left leg links positions','NumberTitle','off')
for ii=1:6
    subplot(2,3,ii);
    hold on
    plot(time,q_left_leg(:,ii),'b');
    plot(time,range_q_left(ii,:)'*ones(1,length(time)),'r')
    xlim([0 (T-Ts)]);
    title(['\theta_',num2str(ii)])
    if min(q_left_leg(:,ii))<range_q_left(ii,1) || max(q_left_leg(:,ii))>range_q_left(ii,2)
        title(['OUT OF RANGE!!!: \theta_',num2str(ii)]);
    end
    xlabel('time (s)')
    ylabel('Position (deg)')
end

%FIXME: put limits
%right leg links position plot
figure('Name','Right arm links positions','NumberTitle','off')
for ii=1:4
    subplot(2,2,ii);
    hold on
    plot(time,q_right_arm(:,ii),'b');
    xlim([0 (T-Ts)]);
    title(['\theta_',num2str(ii)])
    xlabel('time (s)')
    ylabel('Position (deg)')
end

%left leg links position plot
figure('Name','Left arm links positions','NumberTitle','off')
for ii=1:4
    subplot(2,2,ii);
    hold on
    plot(time,q_left_arm(:,ii),'b');
    xlim([0 (T-Ts)]);
    title(['\theta_',num2str(ii)])
    xlabel('time (s)')
    ylabel('Position (deg)')
end

disp('Showing joint trajectories and limits')